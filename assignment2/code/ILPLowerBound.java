import lpsolve.*;

class ILPLowerBound {
    public static double lowerbound(TCPProblem p, BnBNode n) {
        try {
            int numVertices = p.n;
            int numEdges = numVertices * (numVertices-1);
            int numVars = numVertices + numEdges;

            LpSolve solver = LpSolve.makeLp(0, numVars);


            solver.deleteLp();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return 0;
    }
}
