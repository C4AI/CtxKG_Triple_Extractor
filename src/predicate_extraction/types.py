from enum import Enum
import tensorflow as tf

from typing import TypedDict, Union

SentenceInput = list[int]
SentenceInputs = list[SentenceInput]
SentenceMapValue = TypedDict("SentenceMapValue", {"input": SentenceInput, "output": tf.Tensor, "count": int})
SentenceMap = dict[Union[str, int], SentenceMapValue]
ModelInput = list[SentenceInput]


class BIO(Enum):
    B = 0
    I = 1
    O = 2
    S = 3


FormattedTokenOutput = list[Tuple[BIO, float]]
FormattedSentenceOutput = list[FormattedTokenOutput]
