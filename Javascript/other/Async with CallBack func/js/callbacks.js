const astrosUrl = "http://api.open-notify.org/astros.json";
const wikiUrl = "https://en.wikipedia.org/api/rest_v1/page/summary/";
const peopleList = document.getElementById("people");
const btn = document.querySelector("button");

//make an ajax request
function getJson(url, callback) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", url);
  xhr.onload = () => {
    if (xhr.status === 200) {
      let data = JSON.parse(xhr.responseText);
      callback(data);
    }
  };
  xhr.send();
}
function getProfiles(json) {
  json.people.map((person) => {
    getJson(wikiUrl + person.name, generateHTML);
  });
}
// Generate the markup for each profile
function generateHTML(data) {
  const section = document.createElement("section");
  peopleList.appendChild(section);
  section.innerHTML = `
  <h2>${data.title}</h2>
  <p>${data.description}</p>
  <p>${data.extract}</p>
  `;
}

btn.addEventListener("click", (e) => {
  getJson(astrosUrl, getProfiles);
  e.target.remove();
});
