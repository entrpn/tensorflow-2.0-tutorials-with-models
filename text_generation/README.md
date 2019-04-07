Almost all the work here is copied from https://www.tensorflow.org/alpha/tutorials/sequences/text_generation.

Trained 30 steps. 

Evaluating
If you want to test the already trained models then open Shakespeare_generator_RNN_eval_only.ipynb and run all the cells.

### Build and run Docker image

This was tested on a Macbook.

Serve this model using tornado. I wrote the api to take multiple request and handle them in parallel. However running too many requests in parallel can really slow down the responses . If you want to scale this application you can run this container on kubernetes with multiple pods. 

 - Build

```docker build -t tf-text-generator .```

- Run

```docker run --rm -p 8080:8888 tf-text-generator```

- Test

```curl -d '{"text" : "ROMEO:"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8080```

ROMEO:
IF be done: 'tis though 'tis far to saint Kater to year and marrying eye,
Jound with a questist and stock and great a good
Stand bare a beauty to cheer it in: I'll many anger,
You so you can be rush'
