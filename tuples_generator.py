from config import exparser_result, config
import json


def main():
    with open(config[exparser_result], 'r', encoding="utf8") as f:
        references = json.load(f)
        tuples = getTuples(references)
        print(tuples)


def getTuples(refs):
    result = list()
    for i, ref1 in enumerate(refs["references"]):
        compareRefList = [(ref) for j, ref in enumerate(refs["references"]) if j > i]
        for ref2 in compareRefList:
            if ref2["ref"] == ref1["ref"]:
                t = (ref1, ref2, 1)
            else:
                t = (ref1, ref2, 0)
            result.append(t)

    return result


if __name__ == '__main__':
    main()