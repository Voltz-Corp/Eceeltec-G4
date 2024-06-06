const attendanceStars = document.querySelectorAll(".attendance");
const serviceStars = document.querySelectorAll(".service");
const timeStars = document.querySelectorAll(".time");

const attendanceInput = document.querySelector("#attendance")
const serviceInput = document.querySelector("#service")
const timeInput = document.querySelector("#time")

// Attendance 
attendanceStars.forEach((star, firstIndex) => {
  star.addEventListener("click", () => {
    attendanceStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        attendanceInput.value = secondIndex + 1;
        star.classList.add("active");
      } else {
        star.classList.remove("active");
      }
    });
  })
});

attendanceStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseover", () => {
    attendanceStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.add("hover");
      }
    });
  })
});

attendanceStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseout", () => {
    attendanceStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.remove("hover");
      }
    });
  })
});


// Service 
serviceStars.forEach((star, firstIndex) => {
  star.addEventListener("click", () => {
    serviceStars.forEach((star, secondIndex) => {
      if (firstIndex >= secondIndex) {
        serviceInput.value = secondIndex + 1;
        star.classList.add("active");
      } else {
        star.classList.remove("active");
      }
    });
  })
});

serviceStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseover", () => {
    serviceStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.add("hover");
      }
    });
  })
});

serviceStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseout", () => {
    serviceStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.remove("hover");
      }
    });
  })
});


// Time 
timeStars.forEach((star, firstIndex) => {
  star.addEventListener("click", () => {
    timeStars.forEach((star, secondIndex) => {
      if (firstIndex >= secondIndex) {
        timeInput.value = secondIndex + 1;
        star.classList.add("active");
      } else {
        star.classList.remove("active");
      }
    });
  })
});

timeStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseover", () => {
    timeStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.add("hover");
      }
    });
  })
});

timeStars.forEach((star, firstIndex) => {
  star.addEventListener("mouseout", () => {
    timeStars.forEach((star, secondIndex) => {

      if (firstIndex >= secondIndex) {
        star.classList.remove("hover");
      }
    });
  })
});

