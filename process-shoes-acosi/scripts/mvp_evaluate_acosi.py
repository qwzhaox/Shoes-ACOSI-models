import numpy as np
import pickle
from collections import Counter

sentiment_dict = {"great": "positive", "ok": "neutral", "bad": "negative"}


def extract_spans_mvp(seq, seq_type):
    quints = []
    sents = [s.strip() for s in seq.split("[SSEP]")]
    for s in sents:
        try:
            tok_list = ["[C]", "[S]", "[A]", "[O]", "[I]"]

            for tok in tok_list:
                if tok not in s:
                    s += " {} null".format(tok)
            index_ac = s.index("[C]")
            index_sp = s.index("[S]")
            index_at = s.index("[A]")
            index_ot = s.index("[O]")
            index_ie = s.index("[I]")

            combined_list = [index_ac, index_sp, index_at, index_ot, index_ie]
            arg_index_list = list(np.argsort(combined_list))

            result = []
            for i in range(len(combined_list)):
                start = combined_list[i] + 4
                sort_index = arg_index_list.index(i)
                if sort_index < 4:
                    next_ = arg_index_list[sort_index + 1]
                    re = s[start : combined_list[next_]]
                else:
                    re = s[start:]
                result.append(re.strip())

            ac, sp, at, ot, ie = result

            # if the aspect term is implicit
            if at.lower() == "it":
                at = "null"

            sp = sentiment_dict[sp]

        except ValueError:
            try:
                print(f"In {seq_type} seq, cannot decode: {s}")
                pass
            except UnicodeEncodeError:
                print(f"In {seq_type} seq, a string cannot be decoded")
                pass
            ac, at, sp, ot, ie = "", "", "", "", ""

        quints.append((at, ac, sp, ot, ie))

    return quints


def get_mvp_output(pkl_file, num_path=5):
    with open(pkl_file, "rb") as f:
        (outputs, targets, _) = pickle.load(f)

    targets = targets[::num_path]
    _outputs = outputs
    outputs = []
    for i in range(0, len(targets)):
        o_idx = i * num_path
        multi_outputs = _outputs[o_idx : o_idx + num_path]

        all_quints = []
        for s in multi_outputs:
            all_quints.extend(extract_spans_mvp(seq=s, seq_type="pred"))

        output_quints = []
        counter = dict(Counter(all_quints))
        for quint, count in counter.items():
            # keep freq >= num_path / 2
            if count >= len(multi_outputs) / 2:
                output_quints.append(quint)

        outputs.append(output_quints)

    return outputs
