import fugashi
from mtranslate import translate

def extract_and_translate_particles(text):
    tagger = fugashi.Tagger()

    parsed_text = tagger.parse(text)
    words = parsed_text.split('\n')

    particles = []
    blanked_text = text

    for word in words:
        if '助詞' in word:
            particle = word.split('\t')[0]
            particles.append(particle)
            blanked_text = blanked_text.replace(particle, '___')

    translated_text = translate(text, 'zh')

    return particles, blanked_text, translated_text

def fill_in_the_blanks(particles):
    num_blanks = len(particles)
    user_answers = []

    for i in range(num_blanks):
        user_answer = input(f"请输入第{i+1}个空的答案：")
        user_answers.append(user_answer)

    correct_count = 0

    for i in range(num_blanks):
        if user_answers[i] == particles[i]:
            correct_count += 1

    accuracy = correct_count / num_blanks * 100
    return accuracy, user_answers

japanese_text = input("请输入日语段落：")
particles, blanked_text, translated_text = extract_and_translate_particles(japanese_text)

print("挖空后的文本:", blanked_text)
print("原文本的英文译文:", translated_text)

accuracy, user_answers = fill_in_the_blanks(particles)
print("正确率：", accuracy, "%")
print("正确答案依次是:", particles)
print("用户答案依次是:", user_answers)
