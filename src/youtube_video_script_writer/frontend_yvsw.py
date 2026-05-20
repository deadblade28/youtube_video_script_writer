import streamlit as st

from crew import YoutubeVideoScriptWriter


def main():
    st.title("YouTube Video Script Writer")
    st.sidebar.title("Inputs")

    topic = st.sidebar.text_input("Enter Video Topic")
    target_audience = st.sidebar.text_input("Enter Target Audience")

    if st.sidebar.button("Generate Script"):

        if topic and target_audience:

            inputs = {
                "topic": topic,
                "target_audience": target_audience
            }

            with st.spinner("Generating YouTube Script..."):

                result = YoutubeVideoScriptWriter().crew().kickoff(inputs=inputs)

            st.success("Script Generated Successfully!")

            hooks = result.tasks_output[0].raw
            script = result.tasks_output[1].raw
            titles = result.tasks_output[2].raw

            tab1, tab2, tab3 = st.tabs(
                ["Hooks", "Full Script", "Titles & Thumbnail"]
            )

            with tab1:
                st.text_area("Generated Hooks", hooks, height=300)

            with tab2:
                st.text_area("YouTube Script", script, height=500)

                st.download_button(
                    "Download Script",
                    script,
                    file_name="video_script.md"
                )

            with tab3:
                st.text_area(
                    "Titles & Thumbnail Ideas",
                    titles,
                    height=300
                )

        else:
            st.sidebar.error(
                "Please enter both topic and target audience."
            )


if __name__ == "__main__":
    main()