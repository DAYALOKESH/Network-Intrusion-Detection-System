def describe(attack_type):
    # Example: reuse your existing OpenAI setup
    from openai import OpenAI

    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    completion = client.chat.completions.create(
        model="mlabonne/gemma-7b-it-GGUF",
        messages=[
            {"role": "system", "content": "You are a master of Network security. The inputs passsed to you are being the names of the attack types. you should return about the attack, how it is implemented, how it  can be prevented and how it can be detected, how can it be fixed and some probable causes of the attack"},
            {"role": "user", "content": f"The attack type is {attack_type}"}
        ],
        temperature=0.7,
    )

    llm_output = completion.choices[0].message.content

    return llm_output

