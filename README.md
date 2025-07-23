# Chaingguard testing

Using the tutorial from Chainguard python, make sure I understand how to use their python-dev and python images for building (in the end) Django docker images.

```linky``` and ```octo-facts``` should be mirror images of the tutorial.  ```simple-main``` is my own.

## django5-demo
A basic django v5.x application with Dockerfile to build a ~90mb Django docker image.

## Why
Chainguard images are some of the smallest and most secure around, and come with most everything.  Also, good learning exercise in two-stage builds, etc.

I could have used Alpine, but in the end, Chainguard images are easier and smaller.
