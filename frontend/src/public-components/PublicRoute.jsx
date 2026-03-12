import { useAuth } from '../context/AuthContext';
import { Navigate } from 'react-router-dom';

const PublicRoute = ({ children }) => {

    const { user } = useAuth();

    if (user) {
        return <Navigate to='/parse' />;
    }

    return children;
};

export default PublicRoute;
