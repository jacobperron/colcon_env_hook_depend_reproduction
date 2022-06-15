# colcon_env_hook_depend_reproduction

Reproduction of an issue in colcon where environment hooks are not processed for dependencies during test.

## Steps to reproduce

1. Clone this repo into a workspace

    mkdir -p repro_ws/src
    git clone https://github.com/jacobperron/colcon_env_hook_depend_reproduction.git repro_ws/src/repro

2. Build the workspace

    cd repro_ws
    colcon build

3. Run tests for package `bar`

    colcon test --packages-select bar --event-handlers console_direct+

We expect the test to pass, it fails because the environment variable set by `foo` is not set.
