// Define function to fetch file content from GitHub API
async function getFileContent(fileUrl) {
  const response = await fetch(fileUrl);
  const data = await response.text();
  return data;
}

// Define function to display file content
function displayFileContent(fileContent) {
  const fileDisplay = document.createElement("div");
  fileDisplay.innerHTML = fileContent;
  document.body.appendChild(fileDisplay);
}

// Define function to show submenu options
function showSubmenu(folder) {
  // Hide all submenus
  const submenus = document.querySelectorAll(".submenu");
  submenus.forEach((submenu) => {
    submenu.style.display = "none";
  });

  // Show submenu for selected folder
  const submenu = document.querySelector(`#${folder}-submenu`);
  submenu.style.display = "block";
}

// Add event listeners to dropdown menu links
const dropdownLinks = document.querySelectorAll(".dropdown-item");
dropdownLinks.forEach((link) => {
  link.addEventListener("click", async (event) => {
    event.preventDefault();

    // Get folder name from link href attribute
    const folder = link.getAttribute("href");

    if (folder === "py1") {
      // Show submenu options for py1
      showSubmenu("py1");
    } else if (folder === "py2") {
      // Show submenu options for py2
      showSubmenu("py2");
    }

    // Get content of README.md file for selected folder
    const fileUrl = `https://raw.githubusercontent.com/13Aluminium/python_practicals/main/${folder}/README.md`;
    const fileContent = await getFileContent(fileUrl);

    // Display file content
    displayFileContent(fileContent);
  });
});

// Add event listeners to submenu links
const submenuLinks = document.querySelectorAll(".submenu-item");
submenuLinks.forEach((link) => {
  link.addEventListener("click", async (event) => {
    event.preventDefault();

    // Get file path from link href attribute
    const filePath = link.getAttribute("href");

    // Get content of selected file
    const fileUrl = `https://raw.githubusercontent.com/13Aluminium/python_practicals/main/${filePath}`;
    const fileContent = await getFileContent(fileUrl);

    // Display file content
    displayFileContent(fileContent);
  });
});
