# IT5016_Research_Repository.NABIN GNAWALI

 **Programming Principles Applied**

This code implements various essential programming principles which guarantee its simplicity along with maintenance capabilities as well as scalability features. The following section examines the principle implementation within this codebase.

**1. KISS **
    This process follows a basic approach that starts with getting staff information then moving to item data entry then calculates the total cost before presenting results.
    The program simplicity and ease of maintenance is achieved because it contains only essential tasks.

**2. DRY **
    Here Uniting the duplicated input code into reusable functions remains a possible improvement for this code base. The implementation of the get_item_info() function would eliminate unnecessary repetition in the input process.
    The input prompts should move outside of the main loop to create reusable functions for programming code blocks at multiple locations.

**3. Open/Closed Principle**
    The program needs better extensibility features to avoid modifying existing code base. Our main requisitions_total function remains unaltered yet we can enhance the application by implementing item categorization features together with discount options.

    A better way to make the code more extensible would be through code refactoring that includes implementing additional classes as well as external modules.
    
    **4. Composition > Inheritance**
    Despite its absence of inheritance the code base would benefit from implementing composition in its design structure. The main program logic of your application should connect Staff and Item classes which contain separate attributes and responsibilities.
    A proposed restructuring solution includes developing class structures for Staff and Item elements to improve the handling of independent operations.

**5. Single Responsibility Principle**
    The function requisitions_total combines user-driven operations of obtaining input data with the task of performing calculations into one unit that contradicts the Single Responsibility Principle.
    The proposed refactoring introduces separate functions to perform input management and calculate totals while an additional function shows the output results.
        staff_info() for user interaction.
        calculate_total() for total calculation.

**6. Separation of Concerns**
    The application needs to strengthen its organizational boundaries between different program aspects. User interface handling and business operations share the same function within the current design.

    The system needs a split between input management and item processing and total calculation operations into self-contained units.

7.  **YAGNI (You Aren't Gonna Need It).**
    The code fulfills YAGNI requirements because it exclusively addresses the basic functionality consisting of item gathering and total computation.
    Existing proposal points to extra features addition only when real necessity exists. Further requirements for additional capabilities (such as saving requisition data) will enable code extension at a later time.

8.** Avoid Premature Optimization**
    The implemented code remains straightforward in nature while it concentrates primarily on maintaining correctness and readability. The code performs without excess optimization because it refrains from resolving nonexistent problems.
    Future refactorings should aim for both simplicity and readability rather than focusing on performance improvements since the current codebase requires no optimization.
    
 **9.Refactor, Refactor, Refactor**
This program functions effectively as a simple system framework and Code refactoring repeated multiple times improves both the code structure and readability and maintainability until the development coverage is complete. The outlined procedures will preserve program functionality while making it more efficient and modifying operational simplicity.

**10.Clean Code > Clever Code**

This program emphasizes both code readability and maintainability above all other functions by restricting all methods to elementary approaches. A combination of easily understandable code with basic logical principles enables maintenance work as well as future development improvements of the code base.
