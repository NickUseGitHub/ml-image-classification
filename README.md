# Image classification
> Ref: [https://www.geeksforgeeks.org/python-image-classification-using-keras/](https://www.geeksforgeeks.org/python-image-classification-using-keras/)

## Requisite
- Install Anaconda via Brew
  - [https://gist.github.com/ryanorsinger/7d89ad58901b5590ec3e1f23d7b9f887](https://gist.github.com/ryanorsinger/7d89ad58901b5590ec3e1f23d7b9f887)

- Install jupyter-notebook via Brew
  - [https://saturncloud.io/blog/brew-install-jupyter-notebook/](https://saturncloud.io/blog/brew-install-jupyter-notebook/)

- Install tensorflow
  - [https://stackoverflow.com/questions/71516530/installing-keras-tensorflow2-on-macbook-air-with-apple-m1-chip/73341427#73341427](https://stackoverflow.com/questions/71516530/installing-keras-tensorflow2-on-macbook-air-with-apple-m1-chip/73341427#73341427)


### Get started
- create anaconda environment with this command
```
$ conda create --name tensorflow python=3.8

# Activate environment that you created
$ conda activate tensorflow
```

- start jupyter notebook
```
$ jupyter notebook
```

#### File Structure
```
├── Dockerfile <------ image's blueprint
├── model.h5 <------ built model for image classification
├── predict-output.ipynb <------ test output
├── datasets
│   ├── predict  // we divided class with name of files
│   │   ├── noweapons <------ class for detect object
│   │   └── weapons <------ class for detect object
```

### Build docker
Build docker with this command
```
$ docker build -t <YOUR_IMAGE_NAME>:<TAG_VERSION> .
```

Run docker with this command
```
$ docker run --rm -p 5000:5000 <YOUR_IMAGE_NAME>:<TAG_VERSION>
```

### To run local
```
$ python ./app/app.py
```

### FAQ
- Load model via URL
> [Load weights from URL - https://stackoverflow.com/questions/46283444/load-weights-from-url](https://stackoverflow.com/questions/46283444/load-weights-from-url)



