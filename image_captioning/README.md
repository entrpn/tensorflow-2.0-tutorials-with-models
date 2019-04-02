Almost all the work here is copied from https://www.tensorflow.org/alpha/tutorials/sequences/image_captioning. 

The difference is that I trained these models with the full imageset and set the tokenizer to use 10000 words instead of 5000. 

### Evaluating

If you want to test the already trained models then open Image_captioning_eval_only.ipynb and run all the cells. 

This downloads the tokenizer and model (about 350 mb). In the last cell you can change 'image' to your own images to evaluate the model. 

### Training

If you want to train from scratch, I recommend you just follow the instructions in here https://www.tensorflow.org/alpha/tutorials/sequences/image_captioning.

Or follow my notebook Image_captioning.ipynb.