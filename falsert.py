
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(st):
    '''takes a string(word) and removes unwanted characters from the word'''
    new_st=''

    for char in st:
        if char in punctuation_chars:
            new_char=char.replace(char, '')

        else:
            new_st= new_st+char
    return new_st

def get_neg(st):
    '''Takes a tweet and checks to see the num of negative words'''
    count=0
    st=st.split()
    for word in st:
        word= strip_punctuation(word)
        word= word.lower()
        if word in negative_words:
            count+=1
    return count
def get_pos(st):
    '''takes a tweet and checks to see the number of positive words'''
    count=0
    st=st.split()
    for word in st:
        word= strip_punctuation(word)
        word= word.lower()
        if word in positive_words:
            count+=1
    return count


fhand = open('project_twitter_data.csv')
lines= fhand.readlines()
#print (lines)
new_file = open('resulting_data.csv', 'w')
new_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
new_file.write('\n')
#List containing the number of retweets and the number of replies
nums_rt_rp=[]
#List containing the number of postive words
count_pos=[]
#List containg the number of negative words
count_neg=[]
#List containing the net score(postive count-negative count)
net_score=[]
for line in lines[1:]:
    line= line.strip()
    line= line.split(',')
    nums_rt_rp.append(line[1:])
    count_pos.append(get_pos(line[0]))
    count_neg.append(get_neg(line[0]))
#print (count_neg)
#print (len(count_pos))
for count in range(len(count_pos)):
    #print(count_pos[count])
    #print(count_neg[count])
    net_score.append(count_pos[count]-count_neg[count])
print(len(net_score))
for count in range(len(count_pos)):
    new_file.write('{},{},{},{},{}'.format(nums_rt_rp[count][0],nums_rt_rp[count][1],count_pos[count],count_neg[count],net_score[count]))
    new_file.write('\n')
