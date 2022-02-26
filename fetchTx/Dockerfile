FROM python:3.9-alpine as base
FROM base as builder
RUN pip3 install --user requests 

FROM base
COPY --from=builder /root/.local /root/.local
COPY fetchTx.py .
ENTRYPOINT ["python", "./fetchTx.py"]
