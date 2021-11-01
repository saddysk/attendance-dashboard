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

// weekly
function user_attendance() {
  positivePercent = document.getElementById("positivePercent").value;
  negativePercent = document.getElementById("negativePercent").value;

  let attendance_data = {
    labels: ["Present", "Absent"],
    datasets: [
      {
        backgroundColor: "rgb(145, 190, 221)",
        data: [positivePercent, negativePercent],
        backgroundColor: ["#FCE9B0", "#F1B4AD"],
      },
    ],
  };
  new Chart("user_attendance", {
    type: "doughnut",
    data: attendance_data,
  });
}
user_attendance();

// !!!---  ADMIN SECTION   ---!!!

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
