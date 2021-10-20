import { React, useState, useEffect, useRef } from "react";
import "./SingleImage.css";
import axios from "axios";

export default function SingleImage(props) {
  const id = window.location.pathname.slice(14);

  const [csv, setCsv] = useState("");
  const [imgUrl, setImgUrl] = useState("");
  const [number, setNumber] = useState(1);
  const [names, setNames] = useState("");
  const [coordinates, setCoordinates] = useState([]);
  const [load, setLoad] = useState(false);
  const canvasRef = useRef(null);

  function onFileChange(e) {
    setCsv(e.target.files[0]);
  }
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    canvas.width = 903;
    canvas.height = 657;

    var background = new Image();
    background.setAttribute("crossOrigin", "anonymous");
    background.src = imgUrl;

    background.onload = function () {
      ctx.drawImage(background, 0, 0, 450, 400);

      ctx.font = "15px Arial";
      ctx.textAlign = "left";
      ctx.textBaseline = "top";
      ctx.fillStyle = "black";

      ctx.fillText("Dummy Text", 163, 248);
    };
  });

  useEffect(() => {
    axios
      .get("http://localhost:5000/api/" + id)
      .then((response) => {
        setImgUrl(response.data.profileImg);
        setCoordinates(response.data.coordinates);
        console.log(id);
        console.log(id);
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const onSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("csv", csv);
    await axios
      .post("http://localhost:5000/csv-uploads/", formData, {})
      .then((res) => {
        console.log(res);
      });
  };

  function download() {
    var canvas = document.getElementById("myCanvas");
    var url = canvas.toDataURL("image/png");
    var link = document.createElement("a");
    link.download = "filename.png";
    link.href = url;
    link.click();
  }

  //   function loadImages(sources, callback) {
  //     var images = {};
  //     var loadedImages = 0;
  //     var numImages = 0;
  //     for (var src in sources) {
  //       numImages++;
  //     }
  //     for (var src in sources) {
  //       images[src] = new Image();
  //       images[src].onload = function () {
  //         if (++loadedImages >= numImages) {
  //           callback(images);
  //         }
  //       };
  //       images[src].src = sources[src];
  //     }
  //   }

  //   var sources = {
  //     image1: imgUrl,
  //   };
  //   loadImages(sources, function (images) {
  //     context.drawImage(
  //       images.image1,
  //       coordinates[0],
  //       coordinates[1],
  //       coordinates[2],
  //       coordinates[3]
  //     );
  //   });
  // };

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

      <canvas ref={canvasRef} id="myCanvas" width="578" height="200"></canvas>
      <button className="btn btn-primary" onClick={download}>Download</button>
    </div>
  );
}
