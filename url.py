import streamlit as st
from urllib.parse import urlparse
import requests
import geocoder


st.set_page_config(page_title='URL Opener', page_icon='url.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def parse():
    def parse_url(url):
        parsed_url = urlparse(url)
        return parsed_url

    st.markdown(
        "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>URL Parser</h1></center>",
        unsafe_allow_html=True)

    url_input = st.text_input("Enter a URL")

    if st.button("Parse URL"):
        if url_input:
            parsed_url = parse_url(url_input)

            col1, col2, col3, col4 = st.columns(4)
            col1.write("Scheme")
            col1.write(parsed_url.scheme)

            col2.write("Netloc")
            col2.write(parsed_url.netloc)

            col3.write("Path")
            col3.write(parsed_url.path)

            col4.write("Params")
            col4.write(parsed_url.params)

            col1.write("Query")
            col1.write(parsed_url.query)

            col2.write("Fragment")
            col2.write(parsed_url.fragment)

            col3.write("Username")
            col3.write(parsed_url.username)

            col4.write("Password")
            col4.write(parsed_url.password)

            col1.write("Hostname")
            col1.write(parsed_url.hostname)

            col2.write("Port")
            col2.write(parsed_url.port)
        else:
            st.warning("Please enter a URL to parse.")

        st.markdown("---")


def ip():
    def get_ip_details(ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return data

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>IP Lookup</h1></center>",
            unsafe_allow_html=True)

        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 12px;'>Click the button below to "
            "automatically detect your IP address and view the details.</h1></center>",
            unsafe_allow_html=True)
        st.markdown(
            "<style>.stButton>button {margin: 0 auto; display: block;}</style>",
            unsafe_allow_html=True
        )

        if st.button("Detect IP"):
            # with st.spinner("Performing IP lookup..."):
            try:
                ip = requests.get('https://api.ipify.org').text
                st.markdown(f"<p style='text-align: center;'>Performing IP lookup for your IP: {ip}</p>",
                            unsafe_allow_html=True)
                st.markdown("---")

                ip_details = get_ip_details(ip)

                col1, col2, col3, col4 = st.columns(4)

                col1.write(f"IP: {ip_details['query']}")
                col2.write(f"City: {ip_details['city']}")
                col3.write(f"Region: {ip_details['regionName']}")
                col4.write(f"Country: {ip_details['country']}")

                col5, col6, col7, col8 = st.columns(4)

                col5.write(f"Latitude: {ip_details['lat']}")
                col6.write(f"Longitude: {ip_details['lon']}")
                col7.write(f"ISP: {ip_details['isp']}")
                col8.write(f"Host: {ip_details.get('reverse', 'N/A')}")

                col9, col10, col11, col12 = st.columns(4)

                col9.write(f"DNS: {st.experimental_get_query_params().get('dns', ['No'])[0]}")
                col10.write(f"Proxy: {st.experimental_get_query_params().get('proxy', ['No'])[0]}")
                col11.write(f"Anonymizer: {st.experimental_get_query_params().get('anonymizer', ['No'])[0]}")
                col12.write(f"Blacklist: {st.experimental_get_query_params().get('blacklist', ['No'])[0]}")

                location_info = f"{ip_details['city']}, {ip_details['regionName']}, {ip_details['zip']}, {ip_details['country']}"
                st.markdown("<h3 style='text-align: center; position: fixed; bottom: 0; left: 0; right: 0; font-size: "
                            "medium;'>{}</h3>".format(location_info), unsafe_allow_html=True)

            except requests.exceptions.RequestException:
                st.write("Unable to detect your IP address. Please try again later.")

    if __name__ == "__main__":
        main()



def main():
    st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    font-family: Comic Sans MS;
                }
            </style>
            <p class="sidebar-text">URL</p>
        """, unsafe_allow_html=True)
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0DdA5kwwHYQXoAZ-9rvhbMPVL82cn7xR4eg&usqp=CAU",
        use_column_width=True)
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>URL "
                "Opener</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One", ["URL Parser", "IP Lookup"])

    if selected_sidebar == "URL Parser":
        parse()
    elif selected_sidebar == "IP Lookup":
        ip()

    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 12px;'>Because of free hosting he  "
                        "is showing his own "
                        "IP address...</h1></center>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
