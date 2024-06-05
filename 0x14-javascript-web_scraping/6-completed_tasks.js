#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  if (error) {
    console.error("Error fetching data:", error);
    process.exit(1);
  }

  const todos = JSON.parse(body);

  // Concisely calculate completed tasks per user
  const completedPerUser = todos.reduce((acc, todo) => {
    if (todo.completed) {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    }
    return acc;
  }, {});

  // Print results with filtering (if needed)
  const usersWithCompletedTasks = Object.entries(completedPerUser).filter(
    ([userId, count]) => count > 0
  );

  if (usersWithCompletedTasks.length) {
    console.log("Users with completed tasks:");
    console.log(usersWithCompletedTasks);
  } else {
    console.log("No users found with completed tasks.");
  }
});
