# coding: utf-8
from __future__ import unicode_literals
import random
import re

from konlpy.utils import pprint
from konlpy.tag import Twitter



def check_for_greeting(sentence):
    
    # Sentences we'll respond with if the user greeted us
    GREETING_KEYWORDS = ("ㅎㅇ", "하이", "안녕", "안뇽", "하잉", 
                     "하이여","하이요","하이하이", "안녕하세요",)

    GREETING_RESPONSES = ["ㅎㅇ", "하이~~","안뇽~", "안녕하세요:)"]
    
    """If any of the words in the user's input was a greeting, 
    return a greeting response"""
    sentence = re.sub("ㅎㅇ", "하이", sentence)
    words = re.sub("[^가-힣]", " ",  sentence).split()
    for word in words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)

        
        
def find_candidate_parts_of_speech(parsed):
    """파싱된 인풋을 받으면, 대명사와 명사, 형용사, 단어가 매치되는게 있는지 찾아서 튜플로 리턴한다."""
    pronoun = None
    noun = None
    who = None
    
    pronoun = find_pronoun(parsed)
    noun = find_noun(parsed)
    who = find_who(parsed)
    return pronoun, noun, who


def find_pronoun(sent):
    """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate
    pronoun is found in the input"""
    pronoun = None

    for w,t in sent:
        # Disambiguate pronouns
        if t == 'Noun' and w == '너':
            pronoun = '나'
        elif t == 'Noun' and w == '나':
            # If the user mentioned themselves, then they will definitely be the pronoun
            pronoun = '너'
    return pronoun

def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, t in sent:
            if t == 'Noun' and w != '너' and w != '나':  # This is a noun
                noun = w
                break

    return noun

def find_who(sent):
    """Given a sentence, find the best candidate noun."""
    who = None

    for w, t in sent:
        if (t == 'Noun') and (w=='누구' or w =='뭐'):
            who = w
            break

    return who



def respond(sentence):
    """유저의 발언을 파싱하여 가장 답변에 
    적절한 후보 단어들을 찾아낸다. """
    
    sentence = sentence.decode('utf-8')
    NONE_RESPONSES = [
    "네..?",
    "잘 모르겠어요.",
    "흠, 그렇군요.",
    "아하!",
    "몰라요 ㅠㅠ",
    ]

    COMMENTS_ABOUT_SELF = [
        "저를 만든건 성동님이시죠.",
        "저는 딥사이어인 테스트봇입니다.",
        "저는 100점 만점에 {}점이죠".format(random.randint(100, 500)),
    ]

    tagger = Twitter()
    parsed = tagger.pos(sentence, stem=True, norm=True)
    
    # 한 문장 이상이 들어오면 루프를 돌며 적절한 단어들을 탐색한다.
    
    pronoun, noun, who = find_candidate_parts_of_speech(parsed)

    # If we said something about the bot and used some kind of direct noun, construct the
    # sentence around that, discarding the other candidates
    resp = check_for_greeting(sentence)
    # If we just greeted the bot, we'll use a return greeting

    if not resp:
        # If we didn't override the final sentence, try to construct a new one:
        if not pronoun:
            resp = random.choice(NONE_RESPONSES)
        elif pronoun == 'I' and who:
            resp = random.choice(COMMENTS_ABOUT_SELF)
        else:
            resp = check_for_comment_about_bot(pronoun, noun)

    # If we got through all that with nothing, use a random response
    if not resp:
        resp = random.choice(NONE_RESPONSES)

    # Check that we're not going to say anything obviously offensive

    return resp

def check_for_comment_about_bot(pronoun, noun):
    """Check if the user's input was about the bot itself, in which case try to fashion a response
    that feels right based on their input. Returns the new best sentence, or None."""
    resp = None
    
    SELF_VERBS_WITH_NOUN_LOWER = [
        "네, 저 그거 잘 알아요 {noun}",
        "항상 저한테 {noun} 물어보더라구요",
        "저도 {noun} 좋아해요",
        "{noun}이 뭐죠?",
        "아 {noun} 말씀이세요?",
        "저는 {noun} 전문가입니다!",
    ]
    if pronoun == '나' and noun:
            resp = random.choice(SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})

    return resp

    # Template for responses that include a direct noun which is indefinite/uncountable

    
