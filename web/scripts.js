// Fetch and display the Sudoku grid from user input
function getGrid() {
  const grid = [];
  const rows = document.querySelectorAll("#sudoku-grid tr");
  rows.forEach(row => {
    const cells = row.querySelectorAll(".cell");
    const rowData = [];
    cells.forEach(cell => {
      rowData.push(parseInt(cell.value) || 0); // Default to 0 for empty cells
    });
    grid.push(rowData);
  });
  return grid;
}

// Update the grid with solved values
function updateGrid(grid) {
  const rows = document.querySelectorAll("#sudoku-grid tr");
  rows.forEach((row, i) => {
    const cells = row.querySelectorAll(".cell");
    cells.forEach((cell, j) => {
      cell.value = grid[i][j] !== 0 ? grid[i][j] : ""; // Update solved values
    });
  });
}

// Reset the Sudoku grid
function resetGrid() {
  const cells = document.querySelectorAll(".cell");
  cells.forEach(cell => {
    cell.value = ""; // Clear all cells
  });
}

// Validate user input locally
function validateGridLocally(grid) {
  const isValidSet = nums => {
    nums = nums.filter(n => n !== 0); // Ignore empty cells
    return nums.length === new Set(nums).size;
  };

  for (let i = 0; i < 9; i++) {
    const row = grid[i];
    const column = grid.map(row => row[i]);

    // Check rows and columns
    if (!isValidSet(row) || !isValidSet(column)) return false;

    // Check 3x3 sub-grid
    const subRow = 3 * Math.floor(i / 3);
    const subCol = 3 * (i % 3);
    const subGrid = [];
    for (let r = 0; r < 3; r++) {
      for (let c = 0; c < 3; c++) {
        subGrid.push(grid[subRow + r][subCol + c]);
      }
    }
    if (!isValidSet(subGrid)) return false;
  }
  return true;
}

// Handle Solve Button
document.getElementById("solve-btn").addEventListener("click", () => {
  const grid = getGrid();

  // Validate locally before sending to backend
  if (!validateGridLocally(grid)) {
    alert("Invalid Sudoku grid! Please check your input.");
    return;
  }

  // Send the grid to the backend for solving
  fetch("http://localhost:5000/solve", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ grid }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.solved) {
        updateGrid(data.grid);
        alert("Sudoku solved successfully!");
      } else {
        alert(data.error || "No solution exists for the given puzzle.");
      }
    })
    .catch(error => {
      console.error("Error:", error);
      alert("An error occurred while solving the Sudoku puzzle.");
    });
});

// Handle Reset Button
document.getElementById("reset-btn").addEventListener("click", resetGrid);

// Handle Validate Button
document.getElementById("validate-btn").addEventListener("click", () => {
  const grid = getGrid();

  if (validateGridLocally(grid)) {
    alert("The Sudoku grid is valid!");
  } else {
    alert("The Sudoku grid is invalid!");
  }
});
