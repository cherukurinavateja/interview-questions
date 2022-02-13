import json
import re
def phrasel_search(P, Queries):
    # Write your solution here
    ans = []
    # Iterating through each query
    for q in Queries:
        temp_ans = []
        # Iterating through each phrase
        for phrase in P:
            words = phrase.split(" ")
            start = words[0]
            end = words[-1]
            # Using regex to fing the substring
            regex = r'@\ (.*?)$'.replace("@", start).replace("$", end)
            substrings = re.findall(regex, q)
            for substr in substrings:
                substr = start + " " + substr + end
                substr_split = substr.split(" ")
                if (len(substr_split) == len(words)) or (len(substr_split) == len(words)+1):
                    temp_ans.append(substr)
        ans.append(temp_ans)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print(returned_ans)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
