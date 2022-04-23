import torch
import torch.nn as nn
from torch.autograd import Variable
import argparse
import os
import re
from tqdm import tqdm

from helper import *
from model import *
from generate import *

from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('filename', type=str)
argparser.add_argument('--model', type=str, default="gru")
argparser.add_argument('--n_epochs', type=int, default=2000)
argparser.add_argument('--print_every', type=int, default=100)
argparser.add_argument('--hidden_size', type=int, default=100)
argparser.add_argument('--n_layers', type=int, default=2)
argparser.add_argument('--learning_rate', type=float, default=0.01)
argparser.add_argument('--chunk_len', type=int, default=200)
argparser.add_argument('--batch_size', type=int, default=100)
argparser.add_argument('--shuffle', action='store_true')
argparser.add_argument('--cuda', action='store_true')
args = argparser.parse_args()

if args.cuda:
    print("Using CUDA")

file, file_len = read_file(args.filename)

def create_vocab(filename):
    f = open(filename,'r')
    file = f.read()
    t = file.lower()
    words = re.split(' |\n|,|\*|!|:|;|-',t)
    unique_words = {}
    j = 0
    for i in range(len(words)):
        if words[i] not in unique_words:
            unique_words[words[i]] = j
            j+= 1
    print(unique_words)
    return unique_words

def random_training_set(chunk_len, batch_size):
    inp = torch.LongTensor(batch_size, chunk_len)
    target = torch.LongTensor(batch_size, chunk_len)
    for bi in range(batch_size):
        start_index = random.randint(0, file_len - chunk_len)
        end_index = start_index + chunk_len + 1
        chunk = file[start_index:end_index]
        inp[bi] = char_tensor(chunk[:-1])
        target[bi] = char_tensor(chunk[1:])
    inp = Variable(inp)
    target = Variable(target)
    if args.cuda:
        inp = inp.cuda()
        target = target.cuda()
    return inp, target

def train(inp, target):
    hidden = decoder.init_hidden(args.batch_size)
    if args.cuda:
        hidden = hidden.cuda()
    decoder.zero_grad()
    loss = 0

    for c in range(args.chunk_len):
        output, hidden = decoder(inp[:,c], hidden)
        loss += criterion(output.view(args.batch_size, -1), target[:,c])

    #perplexity = torch.exp(loss.data / args.chunk_len)
    #print("PERPLEXIY:", perplexity)
    #print("LOSS: ", loss.data.item() / args.chunk_len)
    #writer.add_scalar("Perplexity", perplexity, epoch)
    #writer.add_scalar("Loss", loss, epoch)
    loss.backward()
    decoder_optimizer.step()
    
    #return loss.data[0] / args.chunk_len
    return loss.data.item() / args.chunk_len

def save():
    save_filename = os.path.splitext(os.path.basename(args.filename))[0] + '.pt'
    torch.save(decoder, save_filename)
    print('Saved as %s' % save_filename)

# Initialize models and start training
vocab = create_vocab(args.filename)
len_vocab = len(vocab)

decoder = CharRNN(
    len_vocab,
    args.hidden_size,
    n_characters,
    model=args.model,
    n_layers=args.n_layers,
)
decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=args.learning_rate)
criterion = nn.CrossEntropyLoss()

if args.cuda:
    decoder.cuda()

start = time.time()
all_losses = []
loss_avg = 0

try:
    print("Training for %d epochs..." % args.n_epochs)
    for epoch in tqdm(range(1, args.n_epochs + 1)):
        loss = train(*random_training_set(args.chunk_len, args.batch_size))
        loss_avg += loss

        writer.add_scalar('RNN Perplexity', math.exp(loss), epoch)

        if epoch % args.print_every == 0:
            print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / args.n_epochs * 100, loss))
            print(generate(decoder, 'Wh', 100, cuda=args.cuda), '\n')

    print("Saving...")
    save()
    
except KeyboardInterrupt:
    print("Saving before quit...")
    save()
writer.close()