import "./Home.css";
import axios from "axios";
import { React, useState, useEffect } from "react";
import { useHistory, Link } from "react-router-dom";

function App() {
  const [image, setImage] = useState("");
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/api/")
      .then((res) => {
        console.log(res);
        setPhotos(res.data);
        console.log(photos);
      })
      .catch(function (err) {
        console.log(err);
      });
  }, []);
  const onSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("profileImg", image);
    await axios
      .post("http://localhost:5000/api/user-profile", formData, {})
      .then((res) => {
        console.log(res);
      });

    window.location.reload();
  };

  function onFileChange(e) {
    setImage(e.target.files[0]);
  }

  return (
    <div className="container">
      <div className="row">
        <form onSubmit={onSubmit}>
          <div className="form-group">
            <input type="file" onChange={onFileChange} />
          </div>
          <div className="form-group">
            <button className="btn btn-primary" type="submit">
              Upload
            </button>
          </div>
        </form>
      </div>
      {photos.map((photo) => (
        <Link to={"/single-image/" + photo._id}>
          <img src={photo.profileImg} width="200" height="200" />
        </Link>
      ))}
    </div>
  );
}

export default App;
