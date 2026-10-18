const clockInBtn = document.getElementById("clockIn");
const clockOutBtn = document.getElementById("clockOut");
const timerEl = document.getElementById("timer");

let startTime = 0;
let intervalId = null;

function format(ms) {
  const totalSeconds = Math.floor(ms / 1000);
  const h = String(Math.floor(totalSeconds / 3600)).padStart(2, "0");
  const m = String(Math.floor((totalSeconds % 3600) / 60)).padStart(2, "0");
  const s = String(totalSeconds % 60).padStart(2, "0");
  return `${h}:${m}:${s}`;
}

function tick() {
  timerEl.textContent = format(Date.now() - startTime);
}

clockInBtn.addEventListener("click", () => {
  startTime = Date.now();
  tick();
  intervalId = setInterval(tick, 1000);
  clockInBtn.disabled = true;
  clockOutBtn.disabled = false;
});

clockOutBtn.addEventListener("click", () => {
  clearInterval(intervalId);
  intervalId = null;
  clockOutBtn.disabled = true;
  clockInBtn.disabled = false;
});
