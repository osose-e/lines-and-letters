import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// Must match the backend's FIREBASE_DATABASE_URL / databaseURL (same project).
const firebaseConfig = {
  databaseURL: process.env.REACT_APP_FIREBASE_DATABASE_URL || "https://lines-and-letters-game-default-rtdb.firebaseio.com",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);

export default database;