# ==========================================================
# STREAMLIT MOVIE BOOKING APP
# Senior-level architecture
# Single-file, multi-page, rerun-safe, button-only UI
# ==========================================================
# RUN:
# streamlit run app.py
# ==========================================================

import streamlit as st
from datetime import datetime, timedelta
import copy
import random

# ==========================================================
# --------------------- DATA ENGINE ------------------------
# ==========================================================

class MainEngine:
    """
    PURE DATA ENGINE.
    No input()/print().
    Safe for Streamlit reruns.
    """

    def __init__(self, cinema_name, movies, seat_plan, showtimes, category):
        self.cinema_name = cinema_name
        self.movies = movies
        self.base_seat_plan = seat_plan
        self.showtimes = showtimes
        self.category = category

    def get_valid_dates(self):
        today = datetime.today().date()
        return [(today + timedelta(days=i)).strftime("%d/%m/%Y") for i in range(5)]

    def clone_seat_plan(self):
        return copy.deepcopy(self.base_seat_plan)

    def randomize_seats(self, seat_plan, showtime):
        # Prevent double randomization
        factor = 0.5 if "pm" in showtime.lower() else 0.2
        for r in range(len(seat_plan)):
            for c in range(len(seat_plan[r])):
                if seat_plan[r][c] == "O":
                    if random.random() < factor:
                        seat_plan[r][c] = "X"
        return seat_plan

    def rows_labels(self, seat_plan):
        return [chr(i) for i in range(ord("A"), ord("A")+len(seat_plan))]

    def get_price(self, seat_codes):
        total = 0
        for seat in seat_codes:
            letter = seat[0]
            for cat, rows in self.category.items():
                if letter in rows:
                    price = int("".join(filter(str.isdigit, cat)))
                    total += price
        return total


# ==========================================================
# ------------------- THEATRE DATA -------------------------
# ==========================================================

class Cinepolis(MainEngine):
    def __init__(self):
        movies = {
            "1": "In the Middle of the Nights",
            "2": "Hooray",
            "3": "Hell 2.O"
        }
        seat_plan = [
            ["O","X","O","O","X",' ',"O","O","X","O","O"],
            ["O","O","O","X","O",' ',"O","X","O","O","O"],
            ["O","O","X","O","O",' ',"O","O","O","X","O"],
            ["O","X","O","O","O",' ',"O","O","O","O","O"],
            ["O","O","O","O","X",' ',"O","O","X","O","O"],
            ["O","O","O","O","O",' ',"O","X","O","O","O"],
            ["O","O","X","O","O",' ',"O","O","O","O","O"]
        ]
        showtimes = {
            '1':['12:30pm','1:00pm','3:00pm','4:45pm'],
            '2':['9:00am','10:30am','2:00pm','4:00pm'],
            '3':['9:45am','11:00am','1:30pm','5:00pm']
        }
        category = {
            "Rs 450 Premium":['A','B'],
            "Rs 300 Execituve":['C','D','E'],
            "Rs 250 Silver":['F','G']
        }
        super().__init__('Cinepolis',movies,seat_plan,showtimes,category)

class PVR(MainEngine):
    def __init__(self):
        movies = {
            "1":"Coyotes",
            "2":"WARFARE IV",
            "3":"Equalizer"
        }
        seat_plan = [
            ["X","O","X","O","O",' ',"O","X","O","O","X"],
            ["O","O","O","O","X",' ',"X","O","O","O","O"],
            ["O","O","O","X","O",' ',"O","O","O","O","O"],
            ["X","O","O","O","O",' ',"O","X","O","O","O"],
            ["O","X","O","O","X",' ',"O","O","O","X","O"],
            ["O","O","X","O","O",' ',"X","O","O","O","O"],
            ["O","X","O","O","O",' ',"O","O","X","O","O"]
        ]
        showtimes = {
            '1':['8:45am','2:00pm','4:15pm','5:45pm'],
            '2':['10:00am','12:15am','3:20pm','7:00pm'],
            '3':['10:45am','1:00pm','2:30pm','6:00pm']
        }
        category = {
            "Rs 350 Premium":['A','B'],
            "Rs 270 Execituve":['C','D','E'],
            "Rs 190 Silver":['F','G']
        }
        super().__init__('PVR',movies,seat_plan,showtimes,category)

class Mukta_A2(MainEngine):
    def __init__(self):
        movies = {
            "1":"Weapons",
            "2":"The Lost Bus",
            "3":"TRONL: ARES"
        }
        seat_plan = [
            ["O","O","O","X","O",' ',"X","O","X","O","X"],
            ["O","O","O","O","X",' ',"O","X","O","O","O"],
            ["X","O","O","X","O",' ',"O","O","O","O","O"],
            ["O","X","O","X","X",' ',"O","X","O","X","O"],
            ["X","O","X","O","X",' ',"O","O","O","O","X"],
            ["O","X","O","X","O",' ',"O","X","O","X","O"],
            ["X","O","X","O","X",' ',"O","O","O","O","X"]
        ]
        showtimes = {
            '1':['8:30am','9:15:00am','6:00pm','8:45pm'],
            '2':['10:00am','11:30am','4:00pm','7:50pm'],
            '3':['9:45am','2:20am','3:30pm','6:00pm']
        }
        category = {
            "Rs 400 Premium":['A','B'],
            "Rs 290 Execituve":['C','D','E'],
            "Rs 200 Silver":['F','G']
        }
        super().__init__('Mukta_A2',movies,seat_plan,showtimes,category)

CINEMAS = {
    "Cinepolis":Cinepolis,
    "PVR":PVR,
    "Mukta A2":Mukta_A2
}

# ==========================================================
# ------------------- SESSION STATE ------------------------
# ==========================================================

def init_state():
    defaults = {
        "page":1,
        "engine":None,
        "seat_plan":None,
        "selected_theatre":None,
        "selected_movie":None,
        "selected_time":None,
        "selected_date":None,
        "selected_seats":[],
        "payment":None
    }
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k]=v

init_state()

def goto(p):
    st.session_state.page = p
    st.rerun()

# ==========================================================
# ---------------------- PAGE 1 ----------------------------
# ==========================================================

def page_theatre():

    st.title("Select Your Favorite Theatre")

    cols = st.columns(3)

    for i,(name,cls) in enumerate(CINEMAS.items()):
        with cols[i]:
            if st.button(name,use_container_width=True,key=f"theatre_{name}"):

                engine = cls()

                st.session_state.engine = engine
                st.session_state.selected_theatre = name
                st.session_state.selected_date = engine.get_valid_dates()[0]

                goto(2)

# ==========================================================
# ---------------------- PAGE 2 ----------------------------
# ==========================================================

def page_movie():

    engine = st.session_state.engine
    st.title("Choose Movie & Showtime")
    # ---------------- DATE SELECTION ----------------

    st.subheader("Select Date")

    dates = engine.get_valid_dates()

    date_cols = st.columns(len(dates))

    for i, d in enumerate(dates):
        with date_cols[i]:
            if st.button(
                d,
                key=f"date_{d}",
                use_container_width=True,
                type="primary" if st.session_state.selected_date == d else "secondary"
            ):
                st.session_state.selected_date = d
                st.rerun()


    for movie_id, movie_name in engine.movies.items():

        st.subheader(movie_name)

        cols = st.columns(len(engine.showtimes[movie_id]))

        for i,time in enumerate(engine.showtimes[movie_id]):

            with cols[i]:

                if st.button(time,key=f"time_{movie_id}_{time}"):

                    # clone seats fresh
                    plan = engine.clone_seat_plan()

                    # check housefull
                    available = any("O" in row for row in plan)

                    if not available:
                        st.warning("Housefull") 
                        return

                    plan = engine.randomize_seats(plan,time)

                    st.session_state.seat_plan = plan
                    st.session_state.selected_movie = movie_id
                    st.session_state.selected_time = time

                    goto(3)

# ==========================================================
# ---------------------- PAGE 3 ----------------------------
# ==========================================================

def page_seats():

    engine = st.session_state.engine
    plan = st.session_state.seat_plan

    st.title("Select Seats")
    rows_label = engine.rows_labels(plan)

    st.write("Seat Map")

    for r,row in enumerate(plan):

        cols = st.columns(len(row))

        for c,val in enumerate(row):

            with cols[c]:

                if val == ' ':
                    st.write("")
                    continue

                seat_code = f"{rows_label[r]}{c+1}"

                disabled = (val == "X")

                if st.button(
                    "X" if disabled else seat_code,
                    key=f"seat_{r}_{c}", 
                    disabled=disabled,
                    use_container_width=True):

                    if seat_code in st.session_state.selected_seats:
                        st.session_state.selected_seats.remove(seat_code)
                    else:
                        st.session_state.selected_seats.append(seat_code)

    selected = st.session_state.selected_seats
    if selected:
        st.info("Selected Seats: " + ", ".join(selected))
    else:
        st.info("Selected Seats: None")


    if st.button("Confirm Seats",use_container_width=True):

        if not st.session_state.selected_seats:
            st.error("Select at least one seat")
            return 


        # mark seats booked
        for seat in st.session_state.selected_seats:
            r = rows_label.index(seat[0])
            c = int(seat[1:])-1
            plan[r][c] = "X"

        goto(4)

# ==========================================================
# ---------------------- PAGE 4 ----------------------------
# ==========================================================

def page_payment():

    engine = st.session_state.engine

    total = engine.get_price(st.session_state.selected_seats)

    st.title("Payment")

    st.write(f"Total Price: ₹{total}")

    methods = ["Apple Pay","Credit Card","Debit Card","Paypal"]

    cols = st.columns(len(methods))

    for i,m in enumerate(methods):
        with cols[i]:
            if st.button(m,key=f"paymethod_{m}"):
                st.session_state.payment = m

    if st.button("Pay",use_container_width=True):

        if not st.session_state.payment:
            st.error("Select payment method")
            return

        goto(5)

# ==========================================================
# ---------------------- PAGE 5 ----------------------------
# ==========================================================

def page_summary():

    engine = st.session_state.engine

    st.title("Final Ticket Summary")

    st.success("Booking Confirmed")

    st.markdown(f"""
    **Theatre:** {engine.cinema_name}  
    **Date:** {st.session_state.selected_date}  
    **Movie:** {engine.movies[st.session_state.selected_movie]}  
    **Showtime:** {st.session_state.selected_time}  
    **Seats:** {", ".join(st.session_state.selected_seats)}  
    **Payment:** {st.session_state.payment}
    """)

# ==========================================================
# ---------------------- ROUTER ----------------------------
# ==========================================================

page = st.session_state.page

if page == 1:
    page_theatre()
elif page == 2:
    page_movie()
elif page == 3:
    page_seats()
elif page == 4:
    page_payment()
elif page == 5:
    page_summary()
