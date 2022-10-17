# -*- coding: utf-8 -*-

from naver_ai import NaverAI

if __name__ == '__main__':
    naver = NaverAI()

    request_data = {
        'maxTokens': 32,
        'temperature': 0.5,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'restart': '',
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': False
    }

    # for text generation
    preset_text = "한국어: 사과\n영어: Apple\n한국어: 바나나"
    start = "\n영어"
    stopBefore = ["\n한국어"]

    text_gen_req = {"text": preset_text,
                    "start": start,
                    "stopBefore": stopBefore}

    generation_result = naver.execute({**request_data, **text_gen_req})
    generation_result
