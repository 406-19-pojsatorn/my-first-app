import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 📌 1. กำหนดค่าเริ่มต้นใน session_state (4 ข้อ)
for i in range(1, 5):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""


# 📌 2. ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    for i in range(1, 5):
        st.session_state[f"ans{i}_val"] = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 3. ฟังก์ชัน MessageBox (Dialog) ตรวจคำตอบ 4 ข้อ
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    answers = [ans1, ans2, ans3, ans4]
    # เฉลย: ผลไม้ 2 ข้อ (apple, banana) + สิ่งของ 2 ข้อ (pencil, phone)
    solutions = ["apple", "banana", "pencil", "phone"]
    score = 0

    for i, (ans, sol) in enumerate(zip(answers, solutions), 1):
        u_ans = ans.strip().lower()
        if u_ans == sol:
            st.success(f"✅ ข้อ {i}: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ {i}: ยังไม่ถูกต้อง (คุณตอบ '{u_ans}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} / 4 คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 📌 4. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 📌 5. แถบแสดงเวลานับถอยหลัง (30 วินาที)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 📌 6. ช่องรับคำตอบ (ผลไม้ 2 ข้อ + สิ่งของ 2 ข้อ)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Monkeys love to eat `b _ n _ n a`. 🍌",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: We use a `p _ n c _ l` to draw and write. ✏️",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: We use a `p _ o n e` to call our friends. 📱",
    value=st.session_state.ans4_val,
)

# 📌 7. อัปเดตค่าล่าสุดเข้า session_state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 📌 8. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 📌 9. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นายพสธร แอริตั้ม ละวันนา เลขที่ 19 ม.4/6")
