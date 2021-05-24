# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    ruta = util.Stack()
    ruta.push((problem.getStartState(), "", 0))

    # Un nodo tendra la siguiente estructura:
    #
    #       ((5,5), "DIRECTION", 0)
    #
    # [0] = POSITION
    # [1] = DIRECTION
    # [2] = COST

    # Arreglo que contiene los nodos ya visitados. Se almacenan SOLO COORDENADAS.
    expanded = []
    # Arreglo que tendra el camino a seguir para que pacman llegue a la meta.
    # El contenido del arreglo tiene la siguiente estructura.
    #       [ ( (<Coordenadas>), <Accion>) ]
    # En donde:
    # Coordenadas = El nodo al que debe dirigirse.
    # Accion = En que direccion debe de moverse.
    directions = []
    while not ruta.isEmpty():
        actual_node = ruta.pop()
        directions.append((actual_node[0], actual_node[1]))
        if problem.isGoalState(actual_node[0]):
            # Si llega a la posicion objetivo termina el programa.
            # Se debe eliminar el primer nodo visitado, ya que este no tiene ninguna direccion.
            directions.pop(0)
            # Para enviar las direcciones solo sera necesario almacenar las ACCIONES, 
            # entonces los nodos a los que se mueve ya no son necesarios.
            directions = [direction[1] for direction in directions]
            return directions
        # Ya que no es la meta, se necesita de los hijos a los que puede avanzar el nodo actual.
        hijos = problem.expand(actual_node[0])
        if actual_node[0] not in expanded:
            # Se agregan los nodos de la posicion actual a la pila.
            for hijo in hijos:
                ruta.push(hijo)
            # La posicion actual se almacena en los nodos visitados. 
            expanded.append(actual_node[0]) 
        else:
            # El nodo ya ha sido expandido.
            # Como el nodo ya fue visitado, este debera eliminarse de las direcciones.
            directions.pop()
            # Se verifica si en la nueva posicion Pacman necesita retroceder.
            while True:
                # Se obtiene la ultima direccion que tomo.
                last_node = directions[-1]
                # Se obtienen los hijos de ese ultimo paso
                children = problem.expand(last_node[0])
                # Se verifica si requiere que pacman retroceda.
                backtrack = needBacktrack(last_node[0], children, expanded) 
                # Si necesita volver, elimina la direccion, si no, sigue avanzando.
                if backtrack:
                    directions.pop()
                else:
                    break 
    util.raiseNotDefined()

def needBacktrack(node, children, expanded):
    # El objetivo de esta funcion es para determinar 
    # si el nodo actual aun tiene hijos sin visitar.
    ###################################################

    # True  = Si ya ha visitado a todos sus hijos. (NECESITA RETROCEDER)
    # False = Pacman aun tiene alternativas para poder avanzar. (NO NECESITA RETROCEDER)

    for num_hijo in range(0,len(children),1):
        if children[num_hijo][0] not in expanded:
            return False 
    return True

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
