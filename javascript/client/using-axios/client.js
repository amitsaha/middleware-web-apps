import {
  requestInterceptor,
  responseInterceptor,
  errorInterceptor,
} from "./interceptors.js";
import axios from "axios";

const axiosGithub = axios.create();

axiosGithub.interceptors.request.use(requestInterceptor, errorInterceptor);
axiosGithub.interceptors.response.use(responseInterceptor, errorInterceptor);

axiosGithub
  .get("https://github.com/")
  .then(function (response) {
    console.log("HTTP Response: %s", response.status);
  })
  .catch(function (error) {
    console.log("See error logs");
  });
