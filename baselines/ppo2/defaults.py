def mujoco():
    return dict(
        nsteps=2048,
        nminibatches=4,
        lam=0.95,
        gamma=0.99,
        noptepochs=10,
        log_interval=1,
        ent_coef=0.0,
        lr=lambda f: 1e-3 * f,
        cliprange=0.1,
        value_network='copy'
    )

def atari():
    return dict(
        nsteps=128, nminibatches=4,
        lam=0.95, gamma=0.99, noptepochs=4, log_interval=1,
        ent_coef=.01,
        lr=lambda f : f * 2.5e-4,
        cliprange=0.1,
    )

def retro():
    return atari()

