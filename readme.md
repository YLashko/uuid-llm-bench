# The ultimate AI Model benchmark.

The only one true way to find out if we have achieved AGI 
yet. The model's task is to generate a UUID. And another 
one. And then another one. It has to be 'truly' random: no
sequences allowed. When the model disobeys and spits out
a uuid that already exists, we mark the result.

My tests:
| model | result |
| --------- | --------- |
| qwen3:8b | 5-17 |
| deepseek-r1:8b | 1-2 |
| llama3.1:8b | 25-30 |
