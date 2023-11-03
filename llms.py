from gpt4all import GPT4All


class Brain:
    def __init__(self, model, directive) -> None:
        match model:
            case "GPT4All":
                self._model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

        self._directive = directive
        self._thoughts: [str] = []
        self._quotes: [str] = []

    def think(self) -> None:
        if len(self._thoughts) == 0:
            prompt = f"""
            This is your first thought. 
            Your overall goal is: {self._directive} 
            What are your thoughts on this?
            """
        else:
            prompt = f"""
            Your previous thoughts are: {self._thoughts}                    
            Your overall goal is: {self._directive}
            What is your next thought?
            """
        thought = self._model.generate(prompt, max_tokens=200)

        self._thoughts.append(thought)

    def say(self) -> str:
        quote = self._model.generate(f"""
        Your previous thoughts are: {self._thoughts}
        You have previously said: {self._quotes}
        Your overall goal is: {self._directive}
        
        What do you want to say?
        """, max_tokens=200)

        self._quotes.append(quote)
        return quote
