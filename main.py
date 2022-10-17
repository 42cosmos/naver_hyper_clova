# -*- coding: utf-8 -*-

from naver_ai import NaverAI

if __name__ == '__main__':
    naver = NaverAI()
    preset_text = "기분 진짜 좋다"

    request_data = {
        'text': preset_text,
        'maxTokens': 32,
        'temperature': 0.5,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '',
        'restart': '',
        'stopBefore': [''],
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': False
    }

    response_text = naver.execute(request_data)
    print(response_text)
