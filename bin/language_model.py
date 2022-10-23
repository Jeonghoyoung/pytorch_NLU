'''
- 언어모델 (Language Model) : 주어진 코퍼스 문장들의 likelihood를 최대화 하는 파라미터를 찾아내
                            주어진 코퍼스를 기반으로 언어의 분포를 학습한다.
     - 문장의 출현 확률 모델링 또는 다음 단어 출현 확률 모델링을 구하는것.
        - 문장의 확률은 단어가 주어졌을 때, 다음 단어를 예측하는 확률을 차례대로 곱한 것과 같다.
     - 따라서 언어모델링은 주어진 단어가 있을 때, 다음 단어의 likelihood를 최대화 하는 파라미터를 찾는 과정이라고도 볼 수 있다.

     - 확률값을 근사하는 가장 간단한 방법은 코퍼스에서 빈도를 세는 것.
        - 하지만, 복잡한 문장일수록 코퍼스에서 출현 빈도가 낮아 부정확한 근사가 이루어질 것.
     - 따라서 Markov assumption을 도입하여 확률값을 근사.
        - 학습 코퍼스에서 보지 못한 문장에 대해서도 확률값을 구할 수 있다.
        - n의 크기가 중요하며 보통 3 ~ 4를 사용.

- N-gram 성능을 상승 시키기 위한 방법
    1. Smoothong
        - Add one Smoothing : 1을 더해주어 확률값의 0을 방지.
        - Generalization of Add One Smoothong : 분자에 해당 단어의 unigram 확률에 상수 m을 곱해준 값을 더해주어 사용하고, 분모에 m을 더해주어
                                                값을 산출

    2. Kneser-Ney Discounting


- Interpolation (보간법)
    - 다른 언어 모델을 linear하게 일정 비율로 섞는 것.
    - general domain LM + domain specific LM
     = general domain 에서 잘 동작하는 domain adapted LM

    

'''