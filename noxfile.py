import nox


#
# Development Sessions
#
@nox.session(reuse_venv=True)
def docs(session):
    session.install("-r", "docs/requirements.txt")

    # Generate documentation into `build/docs`
    session.run("sphinx-build", "-b", "dirhtml", "-v", "docs/", "build/docs")
