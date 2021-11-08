#the image to run
FROM gcc:11 as build
#what to create ad dir
WORKDIR /src/
#what to copy and where
COPY *.c *.h /src/
#the command to execute
RUN gcc -o ui main.c

FROM alpine:3 as build-alp
RUN apk update && apk add build-base
WORKDIR /src/
COPY *.c *.h /src/
RUN gcc -o ui main.c

FROM alpine:3 as build-static
RUN apk update && apk add build-base
WORKDIR /src/
COPY *.c *.h /src/
RUN cc -o ui -static main.c

FROM alpine:3 as alpine
COPY --from=build-alp /src/ui /bin_alpine/ui
ENTRYPOINT ["/bin_alpine/ui"]

FROM scratch as extra-slim
COPY --from=build-static /src/ui /ui
ENTRYPOINT ["/ui"]

FROM debian:stable-slim as slim
                   #source  destination
COPY --from=build /src/ui /bin/ui
#what to do when running th image
ENTRYPOINT ["/bin/ui"]
#if i have argument, by default, if i add another agrument, it'll replaces the one by default
# CMD ["WORLD"]




#remember to allwayd ad --rm in the command in order to delete the container after the excution
# docker build --target slim --tag hello_world_c . "to build the image with a name-tag and a chosen target"
# docker run -it --rm hello_world_c "to excute the built image and delete the container after the excution"
# docker images "to see my images"
# docker run -it --name devc2 -v C:\Users\Utilisateur\Documents\M2\devOps\cours2:/src gcc:11 bash "to create un image and run it in bash"0
# docker exec -it crypto sh "éxecuter un contenaire qui tourne dans un shell"
