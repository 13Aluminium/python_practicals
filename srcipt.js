function showSubmenu(folder) {
  // Hide all submenus
  const submenus = document.querySelectorAll(".submenu");
  submenus.forEach((submenu) => {
    submenu.style.display = "none";
  });

  // Show the selected submenu
  const selectedSubmenu = document.querySelector(`#${folder}-submenu`);
  selectedSubmenu.style.display = "block";

  // Display the files in
