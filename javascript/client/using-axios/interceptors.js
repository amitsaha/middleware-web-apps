export const requestInterceptor = function (requestConfig) {
  requestConfig.startTime = Date.now();
  console.log("url=%s method=%s", requestConfig.url, requestConfig.method);
  return requestConfig;
};

export const responseInterceptor = function (response) {
  console.log(
    "url=%s method=%s status=%s latency=%s",
    response.config.url,
    response.config.method,
    response.status,
    Date.now() - response.config.startTime
  );
  return response;
};

export const errorInterceptor = function (error) {
  if (error.response) {
    console.log(
      "url=%s method=%s error=%s status=%s",
      error.response.config.url,
      error.response.config.method,
      error.response.data,
      error.response.status
    );
  } else if (error.request) {
    console.log(error.request);
  } else {
    console.log("Error", error.message);
  }
  return Promise.reject(error);
};
