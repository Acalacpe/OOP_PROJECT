from analyzer import PasswordAnalyzer
from patterns import has_sequence, has_repetition
from entropy import calculate_entropy
from feedback import check_dataset

class StrengthEvaluator:
    def __init__(self, password):
        self.password = password
        self.analyzer = PasswordAnalyzer(password)

    def evaluate(self):
        score = 0

        score += min(self.analyzer.length() * 3, 30)

        if self.analyzer.has_uppercase():
            score += 7
        if self.analyzer.has_lowercase():
            score += 7
        if self.analyzer.has_number():
            score += 7
        if self.analyzer.has_special():
            score += 7

        if has_sequence(self.password):
            score -= 5

        if has_repetition(self.password):
            score -= 5

        dataset_results = check_dataset(self.password)

        penalty = 0
        max_penalty = 20

        if dataset_results:
            for category, words in dataset_results.items():
                if category == "passwords":
                    penalty += 10 * len(words)
                elif category == "names":
                    penalty += 7 * len(words)
                elif category == "dictionary":
                    penalty += 5 * len(words)

        score -= min(penalty, max_penalty)

        entropy = calculate_entropy(self.password)

        if entropy > 60:
            score += 7
        elif entropy > 40:
            score += 5

        score = max(0, min(score, 50))

        if score < 15:
            strength = "Very Weak"
        elif score < 25:
            strength = "Weak"
        elif score < 40:
            strength = "Medium"
        else:
            strength = "Strong"

        return strength, score, entropy