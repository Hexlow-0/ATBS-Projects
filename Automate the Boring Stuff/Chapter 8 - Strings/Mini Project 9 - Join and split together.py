
comma_data = "john,smith,28,sydney,premium"
pipe_data = "ALICE|O'BRIEN|34|MELBOURNE|STANDARD"
spaced_data = "charlie   brown   41   brisbane   basic"

comma_data = " | ".join(comma_data.title().split(','))

print(comma_data)

pipe_data = ", ".join(pipe_data.lower().split('|'))

print(pipe_data)

spaced_data = (spaced_data.title()).split()

spaced_data = ', '.join(spaced_data)

print(spaced_data)


