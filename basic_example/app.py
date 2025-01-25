import streamlit as st


def hello_world() -> str:
    return "Hello World! This is a simple code that will be used to help me with my first contact with Docker."


def main() -> None:
    st.write(hello_world())


if __name__ == "__main__":
    main()
