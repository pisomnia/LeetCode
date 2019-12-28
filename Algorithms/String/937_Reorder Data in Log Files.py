class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
        """
        letter_log = []
        digit_log = []
        for log in logs:
            temp=log.split(" ")
            if temp[1].isalpha():
                letter_log.append((" ".join(temp[1:]),temp[0]))
            else:
                digit_log.append(log)
        letter_log.sort()
        return [letter[1]+" "+letter[0] for letter in letter_log]+digit_log