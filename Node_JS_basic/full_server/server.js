import express from 'express';
import router from './routes';

const app = express();
const PORT = 1245;

app.use('/', router);

app.listen(PORT);

export default app;
