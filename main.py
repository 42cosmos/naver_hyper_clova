# -*- coding: utf-8 -*-

from naver_ai import NaverAI

if __name__ == '__main__':
    naver = NaverAI()
    preset_text = "한국어: 사과\n영어: Apple\n한국어: 바나나"

    request_data = {
        'text': preset_text,
        'maxTokens': 32,
        'temperature': 0.5,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '\n영어',
        'restart': '',
        'stopBefore': ["\n한국어"],
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': False
    }

    response_text = naver.execute(request_data)
    print(response_text)
