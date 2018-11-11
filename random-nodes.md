# Rough Notes

## Points to make

- Premature optimization
- Algorithmic complexity
- Low-hanging fruit (e.g. NumPy for numeric calculations)
- Degradation of code clarity when optimizing (Carmack)
- Trace it all with profiling, quickly iterate with timeit
- Use-case
    - Waldo profiling
    - Bootstrapping our programs (slice out the loading of telephone numbers)
    - aiohttp requests
- Profiling types
    - deterministic
        - call-based (profile)
        - line-based (?)
    - statistical
        - sample the call-stack
    - memory
        - ?
- Profiling tools
    - standard library only (profile -> pstats)
    - profile + better viz (snakeviz)
    - django-integrated (silk?)
    - pyspy
- General hints
    - When using deterministic profilers, don't profile hour-long code -> the profiler can slow the code by roughly 30% to 300%, and information on all the calls are recorded. I like the dozens-of-seconds range, but 3-300 seconds can work if your input isn't that easy to adjust. Cut down your input to something that runs in the dozens so you can iterate on changes reasonably quickly. Be aware that when you shrink the input, the smaller/lower-algorithmic components of your code may appear more dominant.
    - When using call-based profilers, doing too much in one function may make it harder to see where the time is being spent.

- threaded code

## Outline

### When to profile

- You don't know why it's slow: If you're making a single call to a numpy or scikit function call that takes minutes to run, that's why it's slow.

- Great for deeply nested code

- Can help spot slow algorithms


### stdlib cProfile/profile

Wrap code you want to profile in a `profile.Profile`'s `enable()` and `disable()` methods

The code logs *calls*, not time spent on lines; i.e it's a *stack* profiler, not a *line* profiler.

###
