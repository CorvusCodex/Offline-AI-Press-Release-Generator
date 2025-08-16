from utils import run_llama

def press_release(news):
    prompt = f"Write a professional press release about:\n{news}"
    return run_llama(prompt)

if __name__ == "__main__":
    news = input("News/event: ")
    print(press_release(news))
