// Graph Resource - https://www.chartjs.org/docs/latest/charts/bar.html
// Location: https://www.youtube.com/watch?v=J-lUOFXxG_0
// OpenCage: https://opencagedata.com/dashboard#geocoding
// Mail: attendance.dashboard@protonmail.com::WmrpPt3AAU2MA7Z

/* ****** CODE ****** */

// ------- Clock -------
function currentTime() {
  let date = new Date();
  let hh = date.getHours();
  let mm = date.getMinutes();
  let ss = date.getSeconds();

  //   AM / PM
  /*
  let session = "AM";

  if (hh > 12) {
    session = "PM";
  }
*/

  hh = hh < 10 ? "0" + hh : hh;
  mm = mm < 10 ? "0" + mm : mm;
  ss = ss < 10 ? "0" + ss : ss;

  //   let time = hh + ":" + mm + ":" + ss + " " + session;
  let time = hh + " : " + mm + " : " + ss;

  document.getElementById("clock").innerText = time;
  setTimeout(function () {
    currentTime();
  }, 1000);
}
currentTime();

// ------- Date -------
function getDate() {
  let today = new Date(),
    date = String(today.getDate()).padStart(2, "0"),
    month = String(today.getMonth() + 1).padStart(2, "0"),
    year = today.getFullYear();

  today = month + "-" + date + "-" + year;
  document.getElementById("cur_date").innerHTML = `${today}`;
}
getDate();

// ------- Location -------
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Browser not supporting Geolocation.");
  }
}
function showPosition(position) {
  let { latitude, longitude } = position.coords,
    API_KEY = "ab47cee8a04d4152a920e4e683f058f8";

  fetch(
    `https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=${API_KEY}`
  )
    .then((response) => response.json())
    .then((response) => {
      let allDetails = response.results[0].components;
      // console.table(allDetails);
      let { city, country } = allDetails;
      document.getElementById("location").innerHTML = `${city}, ${country}`;
    })
    .catch(() => {
      console.log("Something went wrong");
    });
}
getLocation();

// ------- Attendance Graph -------
/*
let weekly = document.getElementById("weekly_attendance"),
  monthly = document.getElementById("monthly_attendance"),
  week_btn = document.getElementById("week_btn"),
  month_btn = document.getElementById("month_btn");
let school = document.getElementById("school_wise_attendance"),
  individual = document.getElementById("individual_attendance"),
  school_btn = document.getElementById("school_btn"),
  individual_btn = document.getElementById("individual_btn");

function school_view() {
  school_btn.style.background = "navy";
  individual_btn.style.background = "blue";
  school.style.display = "block";
  individual.style.display = "none";
  monthly.style.display = "none";
  weekly.style.display = "none";
}
function individual_view() {
  school_btn.style.background = "blue";
  individual_btn.style.background = "navy";
  school.style.display = "none";
  individual.style.display = "block";
  monthly.style.display = "none";
  weekly.style.display = "none";
}

function weekly_view() {
  week_btn.style.background = "navy";
  month_btn.style.background = "blue";
  weekly.style.display = "block";
  monthly.style.display = "none";
  school.style.display = "none";
  individual.style.display = "none";
}
function monthly_view() {
  month_btn.style.background = "navy";
  week_btn.style.background = "blue";
  monthly.style.display = "block";
  weekly.style.display = "none";
  school.style.display = "none";
  individual.style.display = "none";
}
*/

// weekly
function weekly_attendance() {
  let curr_attendance = 75;
  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [curr_attendance, 100 - curr_attendance],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("weekly_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}
weekly_attendance();

// monthly
/*
function monthly_attendance() {
  let curr_attendance = 85;
  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [curr_attendance, 100 - curr_attendance],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("monthly_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}
monthly_attendance();
*/

/* !!!---  ADMIN DASHBOARD ---!!!   */

// school wise
/*
function school_wise_attendance() {
  let curr_attendance = 77;
  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [curr_attendance, 100 - curr_attendance],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("school_wise_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}
school_wise_attendance();
*/

// individual
/*
function individual_attendance() {
  let curr_attendance = 69;
  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [curr_attendance, 100 - curr_attendance],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("individual_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}
individual_attendance();
*/

// display views for admin page
let schoolView = document.getElementById("school_view"),
  individualView = document.getElementById("individual_view");
// display School View
function displaySchoolView() {
  console.log("school");
  schoolView.style.display = "block";
  individualView.style.display = "none";
}
// display Individual View
function displayIndividualView() {
  console.log("individual");
  individualView.style.display = "block";
  schoolView.style.display = "none";
}
