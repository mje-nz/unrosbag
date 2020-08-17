FROM ros:melodic-ros-core

RUN apt-get update && apt-get install -y --no-install-recommends \
        ros-melodic-geometry-msgs \
        ros-melodic-sensor-msgs \
        ros-melodic-tf && \
    rm -rf /var/lib/apt/lists/*
